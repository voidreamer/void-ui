import { forwardRef, type HTMLAttributes } from 'react'
import { cn } from '../../utils'

export interface ProgressProps extends HTMLAttributes<HTMLDivElement> {
  /** Progress value (0-100) */
  value?: number
  /** Color variant for the bar */
  color?: 'peach' | 'moss' | 'sand' | 'danger'
  /** Size variant */
  size?: 'sm' | 'md' | 'lg'
}

export const Progress = forwardRef<HTMLDivElement, ProgressProps>(
  ({ value = 0, color = 'peach', size = 'md', className, ...props }, ref) => {
    return (
      <div
        ref={ref}
        className={cn(
          'void-progress',
          size !== 'md' && `void-progress--${size}`,
          className,
        )}
        role="progressbar"
        aria-valuenow={value}
        aria-valuemin={0}
        aria-valuemax={100}
        {...props}
      >
        <div
          className={`void-progress__bar void-progress__bar--${color}`}
          style={{ width: `${Math.min(100, Math.max(0, value))}%` }}
        />
      </div>
    )
  }
)

Progress.displayName = 'Progress'
