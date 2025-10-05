package com.kmp.signlangtrans

import androidx.compose.foundation.layout.*
import androidx.compose.material.MaterialTheme
import androidx.compose.material.Text
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

@Composable
fun App() {
    var translatedText by remember { mutableStateOf("번역된 텍스트가 여기에 표시됩니다.") }

    MaterialTheme {
        Column(
            modifier = Modifier.fillMaxSize(),
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.Center
        ) {
            CameraView(
                modifier = Modifier
                    .fillMaxWidth()
                    .weight(4f),
                onResult = { result ->
                    translatedText = result
                }
            )

            // Placeholder for Translated Text
            Box(
                modifier = Modifier
                    .fillMaxWidth()
                    .weight(1f),
                contentAlignment = Alignment.Center
            ) {
                Text(
                    text = translatedText,
                    fontSize = 24.sp
                )
            }
        }
    }
}
