
# Oyster Detector

A Biome/Aura Detector for the Roblox game Sol's RNG.

## Settings

- webhooks  (**Required**)
  - You can create a maximum of 5 webhook URLs to send messages to. Duplicate URLs will be ignored.
  - The URL used to communicate with your discord channel. Use [this tutorial](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks#:~:text=%C2%A0%20Facebook-,Making%20A%20Webhook,-With%20that%20in) if you don't know how to create one.
- private_server_link
  - Your Sol's RNG private server link.
- biome_alerts
  - You can set the value to either "true" or "false" depending on whether you want to recieve webhook messages when that biome is detected.
- time_zone_offset
  - Oyster Detector should automatically detect your timezone, but if it doesn't, you can set the offset manually.
  - Example: If the detector says 12:00 P.M., and the actual time is 1:00 P.M., the offset would be 1.
- ping_on_min_rarity
  - You can set the value to either "true" or "false" depending on whether you want to recieve a ping when you recieve an aura greater than or equal to the min_ping_rarity.
- min_ping_rarity
  - The minimum rarity you want to recieve a ping for.
- user_id
  - Your Discord user ID.
  - Used to ping you when you recieve an aura greater than or equal to the min_ping_rarity.

## How to report bugs

Please use the following format when reporting bugs to [@vex.rng](https://discord.com/users/1018875765565177976) on Discord:
```
- Description of the bug.
- How to replicate the bug.
- When you experienced this bug.
*Attach the log file containing the bug.*
*No personal information is recorded in the log file.*
```
Example (this is not a real bug and is just for demonstration):
```
- Doesn't detect the Spectre aura.
- Equip the Spectre aura and it doesn't detect it.
- March 12th, 2025 | 8:30 P.M.
`file: 03-12-2025 20-30-00 oyster_detector.log`
```

## TBA

- GUI
- Multi-Instance Detecting
- Auto Potion Popping
- Auto Equip
- Auto Item Using

## Credits

- [@vex.rng](https://discord.com/users/1018875765565177976) - Creator
- [@requiredstorage](https://discord.com/users/1014820802241245184) - Tester