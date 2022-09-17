rule _Audio_CD_file_kylmbu
{
	meta:
		description = "Audio_CD file"
	strings:
		$a = {52494646????????43444441666D74}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
