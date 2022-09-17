rule _SA2_Adlib_Module_music_file_stqxve
{
	meta:
		description = "SA2 Adlib Module music file"
	strings:
		$a = {53416454}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
