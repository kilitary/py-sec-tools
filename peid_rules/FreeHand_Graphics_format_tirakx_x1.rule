rule _FreeHand_Graphics_format_tirakx
{
	meta:
		description = "FreeHand Graphics format"
	strings:
		$a = {41474432}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
