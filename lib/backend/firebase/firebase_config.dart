import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/foundation.dart';

Future initFirebase() async {
  if (kIsWeb) {
    await Firebase.initializeApp(
        options: FirebaseOptions(
            apiKey: "AIzaSyBBBpZWH-pS0Z64CucWmVrAGGuOxbJw5HI",
            authDomain: "hackfest25-d0164.firebaseapp.com",
            projectId: "hackfest25-d0164",
            storageBucket: "hackfest25-d0164.firebasestorage.app",
            messagingSenderId: "595029831234",
            appId: "1:595029831234:web:aa00e936b49aefd228c7db"));
  } else {
    await Firebase.initializeApp();
  }
}
