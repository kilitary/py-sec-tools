rule _Amiga_AIFF_8SFX_Audio_file_cbmnri
{
	meta:
		description = "Amiga AIFF 8SFX Audio file"
	strings:
		$a = {464F524D????????3853565856484452}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
