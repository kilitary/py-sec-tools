rule _AVI_movie_file_mixxka
{
	meta:
		description = "AVI movie file"
	strings:
		$a = {52494646????????415649??4C495354}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
