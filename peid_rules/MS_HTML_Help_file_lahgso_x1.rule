rule _MS_HTML_Help_file_lahgso
{
	meta:
		description = "MS HTML_Help file"
	strings:
		$a = {49545346}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
