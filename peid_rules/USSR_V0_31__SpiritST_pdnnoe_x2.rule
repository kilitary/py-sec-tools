rule _USSR_V0_31__SpiritST_pdnnoe
{
	meta:
		description = "USSR V0_31 __ SpiritST"
	strings:
		$a = {000000000000000000000000400000C02E5553535200000000100000????????00100000????????0000000000000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
