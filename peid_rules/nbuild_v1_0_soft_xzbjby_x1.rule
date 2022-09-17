rule _nbuild_v1_0_soft_xzbjby
{
	meta:
		description = "nbuild v1_0 _soft"
	strings:
		$a = {B9????BB????C0????80????43E2}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
