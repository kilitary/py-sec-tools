rule _BDC_HelpSystem_Help_file_xkiehh
{
	meta:
		description = "BDC HelpSystem Help file"
	strings:
		$a = {4244432048656C7053797374656D}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
