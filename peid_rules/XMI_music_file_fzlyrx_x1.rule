rule _XMI_music_file_fzlyrx
{
	meta:
		description = "XMI music file"
	strings:
		$a = {464F524D????????584D4944}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
