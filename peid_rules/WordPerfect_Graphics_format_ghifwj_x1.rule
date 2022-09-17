rule _WordPerfect_Graphics_format_ghifwj
{
	meta:
		description = "WordPerfect Graphics format"
	strings:
		$a = {FF57504310000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
