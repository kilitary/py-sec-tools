rule _Inset_Systems_PIX_Graphics_format_mpqttc
{
	meta:
		description = "Inset Systems PIX Graphics format"
	strings:
		$a = {0300??0000002000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
