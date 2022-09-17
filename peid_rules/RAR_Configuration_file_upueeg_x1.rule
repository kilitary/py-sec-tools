rule _RAR_Configuration_file_upueeg
{
	meta:
		description = "RAR Configuration file"
	strings:
		$a = {52415220434F4E464947}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
