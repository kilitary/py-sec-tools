rule _NextSun_Audio_file_lhmhxz
{
	meta:
		description = "NextSun Audio file"
	strings:
		$a = {2E736E64}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
