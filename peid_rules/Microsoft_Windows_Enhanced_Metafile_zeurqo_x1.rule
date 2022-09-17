rule _Microsoft_Windows_Enhanced_Metafile_zeurqo
{
	meta:
		description = "Microsoft Windows Enhanced Metafile"
	strings:
		$a = {0100000058}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
