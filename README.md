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
    pod 'SteerpathSmartSDK', '1.0.1.8'
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

- Make sure your application Info.plist contains the following 'App Transport Security Settings'. This is done because the SDK is running a local webserver that does not support HTTPS. However all external communications are using HTTPS.
```
<key>NSAppTransportSecurity</key>
<dict>
  <key>NSAllowsArbitraryLoads</key>
  <true/>
  <key>NSAllowsLocalNetworking</key>
  <true/>
</dict>
```

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

2. Replace the **SteerpathSmartSDK.podspec.json** file with your updated file.
3. Run the following command in Terminal:
```
./publish.sh
```
4. You will be prompted with a list of local CocoaPod repositories similar to the one below. Select (type/copy paste) the repository you're updating and hit enter.
```
Attempting to list local cocoapod repositories: 

bitbucket-nimbledevices-steerpath-sdk-ios-podspec
master
bitbucket-nimbledevices-steerpath-smart-sdk-podspec
steerpath-map-sdk-bitbucket


Select repository for publish: 
```

5. You will need to confirm the repository with the next prompt.
```
Are you sure you want to publish to bitbucket-nimbledevices-steerpath-smart-sdk-podspec? (y/n): 
```

6. Publishing/uploading will run. After completion pull and push the changes into git.

7. Great success!

# Feedback, Support & Suggestions
* Contact: support@steerpath.com
