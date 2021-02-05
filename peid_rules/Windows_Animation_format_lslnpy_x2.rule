rule _Windows_Animation_format_lslnpy
{
	meta:
		description = "Windows Animation format"
	strings:
		$a = {52494646????????41434F4E4C495354}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
