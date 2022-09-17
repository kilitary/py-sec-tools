rule _UPX_Protector_v1_0x_pnzkop
{
	meta:
		description = "UPX Protector v1_0x"
	strings:
		$a = {EBEC????????8A064688074701DB7507}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
