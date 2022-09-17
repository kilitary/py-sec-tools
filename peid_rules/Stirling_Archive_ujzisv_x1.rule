rule _Stirling_Archive_ujzisv
{
	meta:
		description = "Stirling Archive"
	strings:
		$a = {135D658C3A}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
