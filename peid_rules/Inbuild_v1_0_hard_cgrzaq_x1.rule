rule _Inbuild_v1_0_hard_cgrzaq
{
	meta:
		description = "Inbuild v1_0 _hard"
	strings:
		$a = {B9????BB????2E????2E????43E2}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
