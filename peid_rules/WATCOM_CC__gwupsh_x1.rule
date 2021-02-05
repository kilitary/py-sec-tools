rule _WATCOM_CC__gwupsh
{
	meta:
		description = "WATCOM CC__"
	strings:
		$a = {BF????8ED781C4????BE????2BF78BC6B1??D3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
