# **Oyster Detector** ![Oyster Detector Logo](https://raw.githubusercontent.com/vexthecoder/OysterDetector/main/oyster_32x28.png)
### A lightweight biome/aura/merchant tracker for Sol's RNG.

<!--TRAFFIC-STATS-START-->
<!--TRAFFIC-STATS-END-->

[![Stars](https://img.shields.io/github/stars/vexthecoder/OysterDetector?style=for-the-badge&logo=github&color=181717&logoColor=white)](https://github.com/vexthecoder/OysterDetector/stargazers)
[![Issues](https://img.shields.io/github/issues/vexthecoder/OysterDetector?style=for-the-badge&logo=github&color=181717&logoColor=white)](https://github.com/vexthecoder/OysterDetector/issues)
[![License](https://img.shields.io/github/license/vexthecoder/OysterDetector?style=for-the-badge&logo=open-source-initiative&logoColor=white&color=2d2d2d)](https://github.com/vexthecoder/OysterDetector/blob/main/LICENSE)
[![Release](https://img.shields.io/github/v/release/vexthecoder/OysterDetector?style=for-the-badge&logo=tag&logoColor=white&color=2d2d2d)](https://github.com/vexthecoder/OysterDetector/releases)
[![Downloads](https://img.shields.io/github/downloads/vexthecoder/OysterDetector/total?style=for-the-badge&logo=github&logoColor=white&color=2d2d2d)](https://github.com/vexthecoder/OysterDetector/releases)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Discord](https://img.shields.io/badge/Discord-Profile-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/users/1018875765565177976)

## **Features**
- **Biome/Aura Detection**: Monitors biome changes and aura equips, filter webhook messages based on rarity or biome
- **Multiple Webhooks**: Supports multiple webhooks to different channels/servers
- **Rarity-Based Pings**: Get notified when equipping rare auras above customizable thresholds
- **Merchant Detection**: Alerts for Mari and Jester appearances (requires setup)
- **Crash/Reconnect Logging**: Tracks Roblox crashes and game disconnections
- **Private Server Integration**: Embeds your server link in alerts for quick joins
- **Detailed Logging**: Comprehensive logs for troubleshooting
- **Background Operation**: Can run minimized in system tray
- **Auto-Updater**: Detects and downloads new versions automatically (with optional launch prompt)

## **System Requirements**
- Windows 10/11
- Roblox installed
- Discord webhook URL(s)

## **Complete Setup Guide**

### **1. Initial Configuration**
1. Download and launch Oyster Detector
2. Navigate to the Webhooks tab
3. Click "Add Webhook" and enter:
   - A descriptive name (for your reference)
   - Your Discord webhook URL (see below for how to create one)

### **Creating Discord Webhooks**
1. Open Discord and go to your server settings
2. Navigate to Integrations → Webhooks
3. Click "New Webhook"
4. Configure:
   - Name (e.g., "Oyster Alerts")
   - Channel for notifications
   - Optional avatar
5. Copy the webhook URL and paste into Oyster Detector

### **2. Detector Configuration**
1. **Private Server Link** (Recommended):
   - Paste your Sol's RNG private server link
   - Enable "Join PS on Start" to auto-join your server when you start Oyster Detector

2. **Biome Alerts**:
   - Check boxes for biomes you want notifications for
   - Note: GLITCHED and DREAMSPACE always send alerts

3. **Aura Ping Settings**:
   - Enable pings if you want @mentions for rare auras
   - Set your Discord User ID (enable Developer Mode in Discord to get this)
   - Configure minimum rarity threshold (e.g., 100000 for 1 in 100k+ auras)

4. **Aura Filter** (Advanced):
   - Fine-tune notifications per aura
   - Set individual auras to Ping, Ignore, or use Default settings

### **3. Merchant Detection Setup**
1. Enable Merchant Detection in the Detector tab
2. When prompted, allow Oyster Detector to configure Roblox FastFlags (Requires Fishstrap/Bloxstrap)
    - To manually configure FastFlags if Oyster Detector cannot, follow these guides:
      - [Fishstrap FastFlags Guide](https://github.com/vexthecoder/OysterDetector/blob/main/fishstrap_fflags.md)
      - [Bloxstrap FastFlags Guide](https://github.com/vexthecoder/OysterDetector/blob/main/bloxstrap_fflags.md)
3. **Restart Roblox** for changes to take effect
4. Configure merchant-specific settings:
   - Enable/disable Mari/Jester detection
   - Set ping preferences for each merchant

### **4. Additional Settings**
- **UTC Offset**: Adjust if timestamps are incorrect
- **Run in Background**: Keep running when window is closed
- **Start on Launch**: Auto-start detection when opening Oyster Detector
- **Verbose Logging**: Enable for detailed debugging
- **Anti-AFK**: Prevents auto-kick by interacting with Roblox after 15 minutes of idle time with options: jump, click, or chat
- **Toast Notifications**: Small popup alerts for in-game events (can be turned on/off in settings)

## **Usage Instructions**
1. Ensure Roblox is running and you're in Sol's RNG
2. Click "Start Detector" in Oyster Detector
3. Status will change to "ACTIVE" (green) when running
4. Notifications will appear in your configured Discord channels and in logs

## **Troubleshooting**
### Common Issues:
- **No detections**:
  - Verify Roblox is running and you're in Sol's RNG
  - Check firewall/antivirus isn't blocking Oyster Detector (this is a common issue)
  - For merchants: Ensure FastFlags were applied and Roblox was restarted
  - If these steps don't resolve the issue, try restarting Oyster Detector

- **Webhook issues**:
  - Verify URLs start with `https://discord.com/api/webhooks/`
  - Test webhook URLs directly using a tool like DiscoHook

- **High CPU Usage**:
  - Close unnecessary applications
  - Restart Oyster Detector

### **How to Report Bugs**
Please include:
```
Description of the bug
Steps to reproduce
When the bug occurred
Attach relevant log files (Settings → Open Logs Directory)
```
Example:
```
Aura detection fails for Spectre
Equip Spectre aura - no detection
2024-06-10 23:30 UTC
`Log file: 06-10-2025 23-30-00 oyster_detector v1.1.2.log`
```

## **Frequently Asked Questions**
**Q: Why aren't merchant alerts working?**  
A: Ensure you:
1. Enabled merchant detection
2. Allowed FastFlag configuration
3. Restarted Roblox after enabling

**Q: How do I get my Discord User ID?**  
A: Enable Developer Mode in Discord settings, then right-click your profile → "Copy User ID"

**Q: Can I use multiple instances?**  
A: Not currently supported - may cause rate limiting and spam

## **Future Features**
- Multi-Instance Support
- Auto Potion/Item Use

## **Credits & Acknowledgements**
### Development
- **vexthecoder** - Creator and lead developer  
  [GitHub](https://github.com/vexthecoder) | [Discord](https://discord.com/users/1018875765565177976)

### Special Thanks
- **@RequiredStorage** - Lead tester
  <br>[Discord](https://discord.com/users/1014820802241245184)
- **Maxstellar** - Original biome macro inspiration  
  [GitHub](https://github.com/maxstellar/maxstellar-Biome-Macro)
- **Noteab** - Macro inspiration  
  [GitHub](https://github.com/noteab/Noteab-Macro)

### Communities
- **Universal Macros**  
  [Discord](https://discord.gg/B3y2PS65y9)
- **Scope Development**  
  [Discord](https://discord.gg/y8k49dH9z8)
- **Sol's Sniper**
  [Discord](https://discord.gg/RPcPUp47YD)

## **Legal Information**
Oyster Detector is not affiliated with Roblox Corporation or Sol's RNG. Use at your own risk. By using this software, you agree that:
- The developer is not responsible for any account actions
- Reverse engineering is prohibited
- No user data is collected or transmitted

For full terms, see the Credits tab in the application.
