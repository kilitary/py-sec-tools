rule _MaskPE_V2_0__yzkzero_mxdpwg
{
	meta:
		description = "MaskPE V2_0 __ yzkzero"
	strings:
		$a = {B818000000648B1883C330C3403E0FB600C1E0??83C0??36010424C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
