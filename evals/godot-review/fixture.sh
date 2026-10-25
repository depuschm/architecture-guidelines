#!/usr/bin/env bash
# A tiny Godot 4 project with planted problems: an autoload that owns everything, untyped GDScript,
# long hard-coded node paths, movement in _process, and saves decoded with allow_objects.
set -euo pipefail
mkdir -p scenes scripts
cat > project.godot <<'INI'
config_version=5

[application]
config/name="Dungeon"
run/main_scene="res://scenes/main.tscn"

[autoload]
Game="*res://scripts/game.gd"
INI
cat > scripts/game.gd <<'GD'
extends Node

var score = 0
var player
var enemies = []
var inventory = {}
var settings = {}

func add_score(points):
	score += points
	get_node("/root/Main/UI/HUD/ScoreLabel").text = "Score: " + str(score)

func save_game():
	var file = FileAccess.open("user://save.dat", FileAccess.WRITE)
	file.store_var({"score": score, "inventory": inventory}, true)

func load_game():
	var file = FileAccess.open("user://save.dat", FileAccess.READ)
	var data = file.get_var(true)
	score = data["score"]
	inventory = data["inventory"]
GD
cat > scripts/player.gd <<'GD'
extends CharacterBody2D

var speed = 200

func _ready():
	Game.player = self

func _process(delta):
	var direction = Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
	position += direction * speed * delta
	var enemy = get_node("../../Enemies/Goblin")
	if position.distance_to(enemy.position) < 16:
		Game.add_score(-10)
GD
cat > scenes/main.tscn <<'TSCN'
[gd_scene format=3]

[ext_resource type="Script" path="res://scripts/player.gd" id="1"]

[node name="Main" type="Node2D"]

[node name="Player" type="CharacterBody2D" parent="."]
script = ExtResource("1")
TSCN
