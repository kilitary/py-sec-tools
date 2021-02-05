rule _VOB_ProtectCD_iwmjrf
{
	meta:
		description = "VOB ProtectCD"
	strings:
		$a = {363E268AC060E8}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
