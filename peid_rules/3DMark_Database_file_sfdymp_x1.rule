rule _3DMark_Database_file_sfdymp
{
	meta:
		description = "3DMark Database file"
	strings:
		$a = {33444D61726B2044617461626173652046696C65}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
