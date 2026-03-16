import os
import subprocess
import tempfile


def apply_watermark(video_path, watermark_path):
    """Aplica watermark centrado na parte inferior do video usando FFmpeg.

    Retorna o caminho do video com watermark.
    """
    tmp_dir = tempfile.mkdtemp()
    output_path = os.path.join(tmp_dir, "output.mp4")

    # Overlay centrado em baixo com 10% de margem inferior
    # Watermark redimensionado para 20% da largura do video
    filter_complex = (
        "[1:v]scale=iw*0.2:-1[wm];"
        "[0:v][wm]overlay=(W-w)/2:H-h-H*0.05[out]"
    )

    cmd = [
        "ffmpeg",
        "-i", video_path,
        "-i", watermark_path,
        "-filter_complex", filter_complex,
        "-map", "[out]",
        "-map", "0:a?",
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "23",
        "-c:a", "aac",
        "-b:a", "128k",
        "-movflags", "+faststart",
        "-y",
        output_path,
    ]

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)

    if result.returncode != 0:
        print(f"FFmpeg error: {result.stderr}")
        raise RuntimeError(f"FFmpeg falhou: {result.stderr[-500:]}")

    return output_path
