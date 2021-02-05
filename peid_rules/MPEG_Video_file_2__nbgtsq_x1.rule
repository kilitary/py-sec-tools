rule _MPEG_Video_file_2__nbgtsq
{
	meta:
		description = "MPEG Video file _2_"
	strings:
		$a = {000001B3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
