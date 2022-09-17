rule _SND_music_file_pbkzdz
{
	meta:
		description = "SND music file"
	strings:
		$a = {0000F82A??00}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
