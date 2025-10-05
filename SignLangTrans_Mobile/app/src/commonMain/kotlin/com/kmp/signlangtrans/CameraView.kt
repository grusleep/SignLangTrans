package com.kmp.signlangtrans

import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier

@Composable
expect fun CameraView(modifier: Modifier, onResult: (String) -> Unit)
