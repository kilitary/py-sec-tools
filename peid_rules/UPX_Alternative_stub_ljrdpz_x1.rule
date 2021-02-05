rule _UPX_Alternative_stub_ljrdpz
{
	meta:
		description = "UPX Alternative stub"
	strings:
		$a = {B9????BE????BFC0FFFD}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
