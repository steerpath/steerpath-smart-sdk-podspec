# Steerpath Smart SDK for iOS.

Copyright Steerpath Ltd. 2018. All rights reserved

# How to install Steerpath Smart SDK via CocoaPods
- Install CocoaPods http://cocoapods.org/
- Create a Podfile in your project root directory and add the following lines:
```
  source 'https://github.com/CocoaPods/Specs.git'
  source 'https://bitbucket.org/nimbledevices/steerpath-mapbox-ios-podspec.git'
  source 'https://bitbucket.org/nimbledevices/steerpath-smart-sdk-podspec.git'
  use_frameworks!  

  target 'YourAppTargetHere' do
    pod 'SteerpathSmartSDK', '1.0.0.1'
  end  
```
- Navigate to your project root directory and type:
```
pod install
```

To do anything meaningful you will need API access to the Steerpath Platform. Currently API access only via request: support@steerpath.com

After receiving your API key, open the .xcworkspace file created in your project root folder.

- Add the following code into your AppDelegate with your API key.
```
//Swift

import SteerpathSmartSDK

func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
   SPSmartSDK.getInstance().start("insert your API key here")
   return true
}

//Objective-C

@import SteerpathSmartSDK;

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    [[SPSmartSDK getInstance] start: @"insert your API key here"];
    return YES;
}
```

- Make sure your application Info.plist contains the following 'App Transport Security Settings'.
```
<key>NSAppTransportSecurity</key>
<dict>
  <key>NSAllowsArbitraryLoads</key>
  <true/>
  <key>NSAllowsLocalNetworking</key>
  <true/>
</dict>
```
This is done because the SDK is running a local webserver that does not support HTTPS. However all external communications are
using HTTPS.

- Make sure you've linked the following iOS frameworks to your application
```
CoreLocation.framework
CoreBluetooth.framework
CoreMotion.framework
```
- Build!

# How to use with Swift
SteerpathSmartSDK framework classes can be included by adding the following to your source code:
```
import SteerpathSmartSDK
```

# How to use with Objective-C
SteerpathSmartSDK framework classes can be included by adding the following to your source code:
```
@import SteerpathSmartSDK;
```

# How to update PodSpec (for Steerpath Developers)

1. If this is your first time updating the PodSpec you need to do the following:
- Clone the examples repository: https://bitbucket.org/nimbledevices/steerpath-smart-sdk-ios-examples
- Follow the instructions in the repository and build one of the examples projects.
- This will download the required CocoaPod dependencies to your system.

2. Replace the **version.txt** and **SteerpathSmartSDK.podspec.json** files with your updated files.
3. Find out the local CocoaPod repository name for this repository. You can use the following commands to find out.

```
cd ~/.cocoapods/repos/
ls
```

4. Run the following script.

```
./update_podspec.sh
```

5. Run the following command by replacing the REPO_NAME with the repository name you found in step 2.

```
pod repo push REPO_NAME SteerpathSmartSDK.podspec.json
```

6. Pull and push the changes into git.

# Feedback, Support & Suggestions
* Contact: support@steerpath.com
