rule _Microsoft_Access_Database_file_bdgmij
{
	meta:
		description = "Microsoft Access Database file"
	strings:
		$a = {000100005374616E64617264204A657420444200}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
