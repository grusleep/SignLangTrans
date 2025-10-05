plugins {
    id("org.jetbrains.kotlin.multiplatform")
    id("com.android.application")
    id("org.jetbrains.compose")
}

kotlin {
    androidTarget {
        compilations.all {
            kotlinOptions {
                jvmTarget = "1.8"
            }
        }
    }
    
    iosX64()
    iosArm64()
    iosSimulatorArm64()

    sourceSets {
        val commonMain by getting {
            dependencies {
                implementation(compose.runtime)
                implementation(compose.foundation)
                implementation(compose.material)
                implementation(compose.ui)
            }
        }
        val androidMain by getting {
            dependencies {
                val cameraxVersion = "1.3.1"
                implementation("androidx.camera:camera-core:${cameraxVersion}")
                implementation("androidx.camera:camera-camera2:${cameraxVersion}")
                implementation("androidx.camera:camera-lifecycle:${cameraxVersion}")
                implementation("androidx.camera:camera-view:${cameraxVersion}")
            }
        }
    }
}

android {
    namespace = "com.kmp.signlangtrans"
    compileSdk = 34
    defaultConfig {
        applicationId = "com.kmp.signlangtrans.android"
        minSdk = 24
        targetSdk = 34
        versionCode = 1
        versionName = "1.0"
    }
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_1_8
        targetCompatibility = JavaVersion.VERSION_1_8
    }
    sourceSets["main"].manifest.srcFile("src/androidMain/AndroidManifest.xml")
}