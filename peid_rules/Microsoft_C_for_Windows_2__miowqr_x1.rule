rule _Microsoft_C_for_Windows_2__miowqr
{
	meta:
		description = "Microsoft C for Windows _2_"
	strings:
		$a = {8CD8??45558BEC1E8ED8575689}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
