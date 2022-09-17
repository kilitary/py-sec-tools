rule _Thinstall_Embedded_V2_2X_V2_308__Jitit__Sign_by_fly_dxdhqk
{
	meta:
		description = "Thinstall Embedded V2_2X_V2_308 __ Jitit _ Sign by fly"
	strings:
		$a = {B8EFBEADDE506A00FF15????????E9ADFFFFFF8BC18B4C2404898829040000C7400C010000000FB64901D1E9894810C7401480000000C204008B442404C7410C010000008981290400000FB64001D1E8894110C741}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
