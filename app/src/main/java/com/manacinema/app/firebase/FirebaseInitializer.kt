package com.manacinema.app.firebase

import android.content.Context
import com.google.firebase.FirebaseApp
import com.google.firebase.FirebaseOptions

object FirebaseInitializer {
    fun initialize(context: Context) {
        try {
            if (FirebaseApp.getApps(context).isEmpty()) {
                val options = FirebaseOptions.Builder()
                    .setApiKey(com.manacinema.app.BuildConfig.FIREBASE_API_KEY)
                    .setApplicationId("1:883004315598:android:37b044a9b001928afabd9f")
                    .setDatabaseUrl("https://manacinema-3192f-default-rtdb.asia-southeast1.firebasedatabase.app")
                    .setProjectId("manacinema-3192f")
                    .setStorageBucket("manacinema-3192f.firebasestorage.app")
                    .setGcmSenderId("883004315598")
                    .build()
                FirebaseApp.initializeApp(context, options)
            }
        } catch (e: Exception) {
            android.util.Log.e("FirebaseInitializer", "FirebaseApp initialization failed", e)
        }
    }
}
