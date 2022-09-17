rule _UPX_Modified_stub_nnolyu
{
	meta:
		description = "UPX Modified stub"
	strings:
		$a = {50BE????????8DBE????????5783CD}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
