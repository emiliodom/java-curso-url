$ErrorActionPreference = 'Stop'

function New-PlaceholderPng {
  param(
    [Parameter(Mandatory=$true)][string]$Path,
    [Parameter(Mandatory=$true)][string]$Title,
    [string]$Subtitle = '',
    [int]$Width = 1200,
    [int]$Height = 420,
    [string]$Background = '#0d6efd'
  )

  Add-Type -AssemblyName System.Drawing

  $dir = Split-Path -Parent $Path
  if (!(Test-Path $dir)) { New-Item -ItemType Directory -Force -Path $dir | Out-Null }

  $bmp = New-Object System.Drawing.Bitmap([int]$Width, [int]$Height)
  $gfx = [System.Drawing.Graphics]::FromImage($bmp)
  $gfx.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
  $gfx.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::ClearTypeGridFit

  $rect = New-Object System.Drawing.Rectangle(0, 0, [int]$Width, [int]$Height)
  $bgColor = [System.Drawing.ColorTranslator]::FromHtml($Background)
  $bgBrush = New-Object System.Drawing.SolidBrush($bgColor)
  $gfx.FillRectangle($bgBrush, $rect)

  # Simple card overlay
  $overlayColor = [System.Drawing.Color]::FromArgb(55, 255, 255, 255)
  $strokeColor = [System.Drawing.Color]::FromArgb(100, 255, 255, 255)
  $cardBrush = New-Object System.Drawing.SolidBrush($overlayColor)
  $pen = New-Object System.Drawing.Pen($strokeColor, 2)
  $cardRect = New-Object System.Drawing.Rectangle(40, 40, [int]($Width - 80), [int]($Height - 80))
  $gfx.FillRectangle($cardBrush, $cardRect)
  $gfx.DrawRectangle($pen, $cardRect)

  $white = [System.Drawing.Color]::FromArgb(245, 255, 255, 255)
  $muted = [System.Drawing.Color]::FromArgb(220, 255, 255, 255)
  $whiteBrush = New-Object System.Drawing.SolidBrush($white)
  $mutedBrush = New-Object System.Drawing.SolidBrush($muted)

  $titleFont = New-Object System.Drawing.Font('Segoe UI', 28, [System.Drawing.FontStyle]::Bold)
  $subFont = New-Object System.Drawing.Font('Segoe UI', 16, [System.Drawing.FontStyle]::Regular)
  $monoFont = New-Object System.Drawing.Font('Consolas', 12, [System.Drawing.FontStyle]::Regular)

  $gfx.DrawString($Title, $titleFont, $whiteBrush, 80, 120)
  if ($Subtitle -ne '') {
    $gfx.DrawString($Subtitle, $subFont, $mutedBrush, 80, 170)
  }
  $gfx.DrawString((Split-Path -Leaf $Path) + ' (auto)', $monoFont, $mutedBrush, 80, [int]($Height - 95))

  $bmp.Save($Path, [System.Drawing.Imaging.ImageFormat]::Png)

  $gfx.Dispose(); $bmp.Dispose(); $bgBrush.Dispose(); $cardBrush.Dispose(); $pen.Dispose();
  $whiteBrush.Dispose(); $mutedBrush.Dispose(); $titleFont.Dispose(); $subFont.Dispose(); $monoFont.Dispose();
}

$root = Split-Path -Parent $PSScriptRoot
$media = Join-Path $root 'media'

New-PlaceholderPng -Path (Join-Path $media 'image1.png') -Title 'Transformación Digital' -Subtitle 'Universidad Rafael Landívar' -Width 1200 -Height 420 -Background '#0d6efd'
New-PlaceholderPng -Path (Join-Path $media 'image2.png') -Title 'Gráficos de color degradado' -Subtitle 'Placeholder (auto-generado)' -Width 1600 -Height 260 -Background '#6610f2'
New-PlaceholderPng -Path (Join-Path $media 'image4.png') -Title 'Ícono' -Subtitle 'Libro abierto' -Width 256 -Height 256 -Background '#0d6efd'
New-PlaceholderPng -Path (Join-Path $media 'image6.png') -Title 'Ícono' -Subtitle 'Internet' -Width 256 -Height 256 -Background '#20c997'
New-PlaceholderPng -Path (Join-Path $media 'image8.png') -Title 'Ícono' -Subtitle 'Rompecabezas' -Width 256 -Height 256 -Background '#ffc107'

Write-Host "OK: PNG placeholders created in $media"