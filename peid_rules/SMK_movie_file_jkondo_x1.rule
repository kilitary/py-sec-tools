rule _SMK_movie_file_jkondo
{
	meta:
		description = "SMK movie file"
	strings:
		$a = {534D4B32}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
