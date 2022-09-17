rule _Microsoft_Resource_Cursors_file_rgakej
{
	meta:
		description = "Microsoft Resource Cursors file"
	strings:
		$a = {00000200010020200000??00??00E802000016}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
