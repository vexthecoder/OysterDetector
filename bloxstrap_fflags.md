# How to Enable Debug FFlags in BloxStrap

To enable Lua debug logging FFlags in BloxStrap, follow these steps:

## Manual Configuration Method

1. Open **BloxStrap**
2. Navigate to **Engine Settings** > **Fast Flag Editor**
3. Click on **Add new**
4. Click on **Import JSON**
4. Paste the following:
```json
{
    "FStringDebugLuaLogLevel": "trace",
    "FStringDebugLuaLogPattern": "ExpChat/mountClientApp",
}
```
5. Click **OK** then **Save** to apply the changes
6. Restart Roblox for the changes to take effect

![BloxStrap Debug FFlags](https://raw.githubusercontent.com/vexthecoder/OysterDetector/main/bloxstrap_fflags_1.png)
![BloxStrap Debug FFlags](https://raw.githubusercontent.com/vexthecoder/OysterDetector/main/bloxstrap_fflags_2.png)