rule _HSC_music_file_pcvnpb
{
	meta:
		description = "HSC music file"
	strings:
		$a = {C8E20420}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
