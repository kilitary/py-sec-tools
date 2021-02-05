rule _Windows_Group_file_jmnqpb
{
	meta:
		description = "Windows Group file"
	strings:
		$a = {504D4343}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
