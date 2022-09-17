rule _MPEG_movie_file_lgqclq
{
	meta:
		description = "MPEG movie file"
	strings:
		$a = {000001BA2FFFFDE6C1801861000001BB}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
