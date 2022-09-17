rule _Microsoft_Windows_Cabinet_file_zgjsff
{
	meta:
		description = "Microsoft Windows Cabinet file"
	strings:
		$a = {4D534346}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
