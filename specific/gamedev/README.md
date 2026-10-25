<!-- rule-prefix: GAMEDEV -->
# Game development (engine-independent)

Scope: architecture concerns that every game shares, whatever the engine: the game loop and time steps, core game patterns, entity-component systems, data-driven design, multiplayer networking, save data, frame budgets, version control for large assets, and accessibility. Engine-specific guidance is in [Unity](../unity/README.md), [Godot](../godot/README.md) and [Unreal Engine](../unreal/README.md), and the [general guidelines](../../general/README.md) still apply.

> Entries are sorted by score from 1 to 10 ([criteria](../../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

No single official guide covers game architecture across engines. These primary sources are the baseline. The rules below combine them and add choices they leave open.

- `8` [Game Programming Patterns](https://gameprogrammingpatterns.com/contents.html) (Robert Nystrom): **the baseline for code structure.** Free online. It covers the game loop, update method, component, event queue, object pool, data locality and more.
- `8` [Fix Your Timestep!](https://gafferongames.com/post/fix_your_timestep/) (Glenn Fiedler, Gaffer On Games): the standard fixed-time-step loop with an accumulator and interpolation.
- `8` [Fast-Paced Multiplayer](https://www.gabrielgambetta.com/client-server-game-architecture.html) (Gabriel Gambetta): **the baseline for client-server netcode.** A four-part series on authoritative servers, client-side prediction and server reconciliation, entity interpolation, and lag compensation.
- `8` [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/): **the baseline for accessibility.** Guidelines grouped as basic, intermediate and advanced, with examples, and advice on [when and how to apply them](https://gameaccessibilityguidelines.com/why-and-how/).
- `8` [Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/xbox/accessibility/guidelines) (Microsoft): best practices developed with the gaming and disability community, for designers, developers and test teams.
- `7` [Networked Physics](https://gafferongames.com/post/introduction_to_networked_physics/) (Glenn Fiedler, Gaffer On Games): compares deterministic lockstep, snapshot interpolation and state synchronisation for networking a simulation.
- `7` [Save Game Best Practices](https://developers.meta.com/vr/documentation/native/ps-save-game-best-practices/) (Meta Horizon OS developer docs): versioning, migration, integrity checks and backups for save files. Apart from the cloud backup section, the advice applies to any platform.
- `6` [ECS FAQ](https://github.com/SanderMertens/ecs-faq) (Sander Mertens, author of Flecs): what an entity component system is, when it helps, and how implementations differ.

## Key rules

### Game loop

- `8` `GAMEDEV-1` **Advance the simulation in fixed time steps, decoupled from the render rate, and interpolate between the last two simulated states when rendering.** Cap the number of steps per frame so that a slow frame can't start a "spiral of death". ([Gaffer On Games, Fix Your Timestep!](https://gafferongames.com/post/fix_your_timestep/), [Nystrom, Game Loop](https://gameprogrammingpatterns.com/game-loop.html))

### Code structure

- `7` `GAMEDEV-2` **Build game entities by composing components, not through deep inheritance hierarchies.** ([Nystrom, Component](https://gameprogrammingpatterns.com/component.html))
- `7` `GAMEDEV-3` **Define entity types and tuning values as data that designers can change without recompiling, not as one subclass per type.** ([Nystrom, Type Object](https://gameprogrammingpatterns.com/type-object.html), [Unity: ScriptableObject data](../unity/code-architecture.md))
- `4` `GAMEDEV-4` **Adopt an entity component system (ECS) deliberately, when you need very large numbers of entities, and prefer an established framework to writing your own.** A home-grown ECS rarely matches the performance of established ones. ([Mertens, ECS FAQ](https://github.com/SanderMertens/ecs-faq), [Unity: Entities package](../unity/code-architecture.md))

### Multiplayer

- `8` `GAMEDEV-5` **In competitive multiplayer games, make the server authoritative: clients send inputs, and the server runs the simulation and sends back the results.** Never trust game state reported by a client. ([Gambetta, Client-Server Game Architecture](https://www.gabrielgambetta.com/client-server-game-architecture.html), [Gaffer On Games, What every programmer needs to know about game networking](https://gafferongames.com/post/what_every_programmer_needs_to_know_about_game_networking/))
- `7` `GAMEDEV-6` **Hide latency with client-side prediction and server reconciliation.** The client applies its own inputs at once and numbers them. When an authoritative update arrives, it starts from that state and re-applies the inputs the server hasn't processed yet. ([Gambetta, Client-Side Prediction and Server Reconciliation](https://www.gabrielgambetta.com/client-side-prediction-server-reconciliation.html))
- `6` `GAMEDEV-7` **Render other players slightly in the past, interpolating between buffered server updates, instead of snapping to each update as it arrives.** ([Gambetta, Entity Interpolation](https://www.gabrielgambetta.com/entity-interpolation.html), [Gaffer On Games, Snapshot Interpolation](https://gafferongames.com/post/snapshot_interpolation/))
- `5` `GAMEDEV-8` **For hit detection in fast-paced shooters, use lag compensation: the server rewinds the world to the moment the shooter saw it and checks the hit there.** ([Gambetta, Lag Compensation](https://www.gabrielgambetta.com/lag-compensation.html))
- `5` `GAMEDEV-9` **Choose deterministic lockstep, which sends only inputs, only if the simulation is bit-for-bit deterministic on every platform you ship to. Otherwise, synchronise state.** Floating-point results can differ between compilers, operating systems and CPUs. ([Gaffer On Games, Deterministic Lockstep](https://gafferongames.com/post/deterministic_lockstep/), [Floating Point Determinism](https://gafferongames.com/post/floating_point_determinism/))

### Save data

- `8` `GAMEDEV-10` **Version the save-data schema from the first release, and migrate older saves to the current version when loading them.** ([Meta, Save Game Best Practices](https://developers.meta.com/vr/documentation/native/ps-save-game-best-practices/))
- `7` `GAMEDEV-11` **Keep the last good save until the new one is completely written, and store an integrity check so that a corrupt or partial save falls back to the previous one.** ([Meta, Save Game Best Practices](https://developers.meta.com/vr/documentation/native/ps-save-game-best-practices/))

### Performance

- `8` `GAMEDEV-12` **Set a frame-time budget for each target platform (33.3 ms at 30 fps, 16.7 ms at 60 fps), and measure against it with a profiler on the target hardware, before and after each optimisation.** ([Unreal Engine, Introduction to performance profiling and configuration](https://dev.epicgames.com/documentation/en-us/unreal-engine/introduction-to-performance-profiling-and-configuration-in-unreal-engine), [Godot, General optimization tips](https://docs.godotengine.org/en/stable/tutorials/performance/general_optimization.html), [Unity: profiling](../unity/content-and-performance.md))
- `5` `GAMEDEV-13` **Pool objects that are created and destroyed often, such as projectiles and particles, instead of allocating and freeing each one.** ([Nystrom, Object Pool](https://gameprogrammingpatterns.com/object-pool.html), [Unity: object pooling](../unity/content-and-performance.md))
- `4` `GAMEDEV-14` **Rearrange data for cache locality only where profiling shows that cache misses cost time.** The resulting code is more complex and less flexible. ([Nystrom, Data Locality](https://gameprogrammingpatterns.com/data-locality.html))

### Version control and assets

- `8` `GAMEDEV-15` **Pick version control that handles large binary assets before the project grows: Git with Git LFS, or a system built for binaries such as Perforce.** GitHub blocks files larger than 100 MiB and recommends keeping repositories under 1 GB. Git LFS stores large files on a separate server and keeps only pointers in Git. The Unreal Editor follows Perforce's check-out workflow. ([GitHub, About large files on GitHub](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github), [Git LFS](https://git-lfs.com/), [Unreal Engine, Using Perforce as source control](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-perforce-as-source-control-for-unreal-engine))
- `7` `GAMEDEV-16` **Lock binary assets that can't be merged, such as levels, textures, models and audio, before editing them: mark their types `lockable` in `.gitattributes` with Git LFS, or check them out exclusively in Perforce.** Concurrent edits to large binary files cause merge conflicts that are very difficult to resolve. ([Git LFS, File Locking](https://github.com/git-lfs/git-lfs/wiki/File-Locking), [Unreal Engine, Using Perforce as source control](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-perforce-as-source-control-for-unreal-engine))

### Accessibility

- `7` `GAMEDEV-17` **Plan accessibility at the design stage: review the Game Accessibility Guidelines before work starts, choose the ones that apply, and schedule early the ones that are costly to add later.** Many guidelines can be met with simple design decisions early on, and retrofitting them later costs significantly more. ([Game Accessibility Guidelines, Why and how](https://gameaccessibilityguidelines.com/why-and-how/))
- `7` `GAMEDEV-18` **Address the four most common complaints first: control remapping, text size, colour blindness and subtitle presentation.** ([Game Accessibility Guidelines, Basic](https://gameaccessibilityguidelines.com/basic/))
- `6` `GAMEDEV-19` **Don't convey essential information by colour alone or by sound alone, and give effects, speech and music separate volume controls.** ([Game Accessibility Guidelines, Basic](https://gameaccessibilityguidelines.com/basic/))
- `5` `GAMEDEV-20` **Use the Xbox Accessibility Guidelines as a test checklist for your game's accessibility features.** ([Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/xbox/accessibility/guidelines))

## Tutorials and further reading

- `7` [Game Engine Architecture](https://www.gameenginebook.com/) (Jason Gregory): a comprehensive book on how game engines are built, from engine subsystems and game world object models to tools and asset pipelines.
- `6` [Accessible Player Experiences (APX)](https://accessible.games/accessible-player-experiences/) (AbleGamers): access patterns for game design, such as Flexible Controllers, Clear Channels and Distinguish This From That.
- `6` [What every programmer needs to know about game networking](https://gafferongames.com/post/what_every_programmer_needs_to_know_about_game_networking/) (Glenn Fiedler): a short history from peer-to-peer lockstep to client-side prediction.
