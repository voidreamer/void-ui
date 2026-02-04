import { forwardRef, type HTMLAttributes, type ReactNode } from 'react'
import { cn } from '../../utils'

export interface BadgeProps extends HTMLAttributes<HTMLSpanElement> {
  /** Badge color variant */
  variant?: 'default' | 'peach' | 'moss' | 'sand' | 'blush' | 'lilac' | 'danger' | 'outline' | 'tech'
  /** Badge size */
  size?: 'sm' | 'md' | 'lg'
  /** Use pill shape */
  pill?: boolean
  children?: ReactNode
}

export const Badge = forwardRef<HTMLSpanElement, BadgeProps>(
  ({ variant = 'default', size = 'md', pill, className, children, ...props }, ref) => {
    return (
      <span
        ref={ref}
        className={cn(
          'void-badge',
          variant !== 'default' && `void-badge--${variant}`,
          size !== 'md' && `void-badge--${size}`,
          pill && 'void-badge--pill',
          className,
        )}
        {...props}
      >
        {children}
      </span>
    )
  }
)

Badge.displayName = 'Badge'
