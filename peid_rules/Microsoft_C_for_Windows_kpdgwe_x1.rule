rule _Microsoft_C_for_Windows_kpdgwe
{
	meta:
		description = "Microsoft C for Windows"
	strings:
		$a = {33ED559A????????0BC074}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
