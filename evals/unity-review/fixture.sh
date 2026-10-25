#!/usr/bin/env bash
# A tiny Unity project with planted problems: a singleton with scene-wide lookups, per-frame
# allocations and lookups in Update, Resources.Load for content, no assembly definitions, no .gitignore.
set -euo pipefail
mkdir -p ProjectSettings Packages Assets/Scripts Assets/Resources/Enemies
printf 'm_EditorVersion: 6000.2.6f1\n' > ProjectSettings/ProjectVersion.txt
printf '{\n  "dependencies": {\n    "com.unity.ugui": "2.0.0"\n  }\n}\n' > Packages/manifest.json
printf 'placeholder prefab\n' > Assets/Resources/Enemies/Goblin.prefab
cat > Assets/Scripts/GameManager.cs <<'CS'
using System.Collections.Generic;
using System.Linq;
using UnityEngine;

public class GameManager : MonoBehaviour
{
    public static GameManager Instance;
    public int score;

    void Awake() { Instance = this; }

    void Update()
    {
        var player = FindObjectOfType<Player>();
        var enemies = new List<Enemy>(FindObjectsOfType<Enemy>());
        var alive = enemies.Where(e => e.health > 0).ToList();
        GameObject.Find("ScoreText").GetComponent<UnityEngine.UI.Text>().text = "Score: " + score;
        if (alive.Count < 3)
        {
            var prefab = Resources.Load<GameObject>("Enemies/Goblin");
            Instantiate(prefab, player.transform.position + Vector3.forward * 10, Quaternion.identity);
        }
    }
}
CS
cat > Assets/Scripts/Player.cs <<'CS'
using UnityEngine;

public class Player : MonoBehaviour
{
    void OnTriggerEnter(Collider other)
    {
        GameManager.Instance.score += 10;
        Destroy(other.gameObject);
    }
}
CS
cat > Assets/Scripts/Enemy.cs <<'CS'
using UnityEngine;

public class Enemy : MonoBehaviour
{
    public int health = 3;
}
CS
