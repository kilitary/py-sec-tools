rule _Video_CD_file_cywfcy
{
	meta:
		description = "Video_CD file"
	strings:
		$a = {52494646????????43445841666D74}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
