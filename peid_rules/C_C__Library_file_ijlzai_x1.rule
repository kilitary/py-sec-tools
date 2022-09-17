rule _C_C__Library_file_ijlzai
{
	meta:
		description = "C_ C__ Library file"
	strings:
		$a = {F00D0000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
